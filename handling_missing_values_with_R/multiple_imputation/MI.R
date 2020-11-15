# A tutorial on the mice package in R for multiple imputation
# Reference: https://uvastatlab.github.io/2019/05/01/getting-started-with-multiple-imputation-in-r/

## mice (Mutliple imputation chained equations)
  # Create a number of imputed (completed) datasets using an imputation model to fill in missing values in different columns
## Different implementations of MI:
  # Amelia and norm packages: Assumes the observed variables follow a multivariate normal distribution.
  # Uses an algroithm to impute missing values by drawing from this assummed distirbution.

  # mice uses conditional MI.  Model the conditional distribution of a ceertain variable given the other variables
  # in an iterative manner.  For more details, refer to this article: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4477955/

  # Workflow of mice:  incomplete data ----- MI ---> 10 sets of imputed data ----> modelling (10 models) ----> pooled results
  

## mice() command creates several complete datasets.  Mice considers each missing value to follow a specific distirbution,
# and draws from this distribution a plausible value to replace the missing value.

# The complete datasets are stored in an object class called "mids" (multiply imputed dataset).  These datasets
# are "copies" of the original dataset with missing values repalced by values from mice().  This however creates
# additional uncertainty since we are now estimating regression coefficients with several different imputed datasets.
# We need to factor in this uncertainty in our estimated coefficients.

# Armed with these (three) imputed datasets (say n=1000 for each), we run OLS regression on these imputed datasets
# separately.  Using with_mids (with multiply imputed dataset) command, we run OLs regression (ex: regress income on age)
# We get 3 estimated coefficents from three regression models.  The 3 coefficients are different than one another
# because each dataset contains different imputed values, and we are uncertain which imputed values are the "true" ones.
# The regresssion outputs are stored in mira object class (multiply imputed repeated analysis).

# Finally, we pool together the 3 coefficients estimated by the imputed dataset into 1 final regression coefficient, and 
# estimate the variance using the pool command.
# We assume the 3 betas have multivariate normal distirbution, and we calculate the variance of the final estimated beta
# by taking into account the within variance (account for the differences in predicted values from the dataset), 
# and between variance (accounting for differences between the 3 datasets).

########################################################################################################################

library(dplyr)
library(mice)
library(foreign) # to import Stata DTA files
library(car)     # for recode

set.seed(137)

# Dependent variable: 
  # Sentiment towards Clinton

## Indepnendent variable: 
  # Occupation: 1: if respondent works in manufacturing; 0: respondent does not work in manufacturing
  # Party ID: 0 strong Democrat,...,6 strong Republican
  # Nationalism: 0 not important,..., 4 extremely important
  # Views on China's rise: 0 Good; 1 Bad
  # Number of Chinese Mergers & Acquistions activity  0-60

# Process data -------------------------------------------------------------------

# Import ANES 2012 dataset
anesimp <- read.dta("data/anesimputation.dta", 
                    convert.factors=FALSE, missing.type = TRUE)

# Replace all values <0 as NA
anesimp<-anesimp %>% mutate_all(~replace(.,.<0,NA))

# Get occupation variable from "anesocc.csv"
anesocc<-read.csv("data/anesocc.csv", sep=";",
                  na.strings =c("", "NA"))

# Get caseid (unique identifier), occupation now ("dem_occnow") and industry now (dem_indnow") columns
anesocc2 <- anesocc %>% select(caseid, dem_occnow,dem_indnow)

# Create a new column called manuf (1: respondent works in manufacturing, 0: otherwise): 
# Categorize any text in dem_occnow and dem_indnow that includes "manu" in it as
# respondents working in manufacturing, with the exception of "manuver"

anesocc2 <- anesocc2 %>% mutate(manuf = case_when((grepl("manu",dem_occnow, useBytes = TRUE)&!grepl("manuver",dem_occnow, useBytes = TRUE)) ~ 1,
                         grepl("manu",dem_indnow, useBytes = TRUE) ~ 1,
                         is.na(dem_occnow) ~ NA_real_, # if entry in dem_occnow is NA
                         is.na(dem_indnow) ~ NA_real_, # if entry in dem_indnow is NA
                         !is.na(dem_occnow) ~ 0, # set all other rows to 0
                         !is.na(dem_indnow) ~ 0))

# Get only the manufacturing column
anesocc2<- anesocc2 %>% select(manuf)

# Add column "manuf" in anesocc2 to anesimp.  The rows of these two datasets are sorted in the same order.
anesimp <- cbind(anesimp,anesocc2)


# import MA data
maimp <-read.dta("data/ma.dta")

anesimp <- merge(x=anesimp, y=maimp, by=c("sample_state"))


# Recode some variables
anesimp$patriot_amident <-recode(anesimp$patriot_amident,
                                 "5=0; 4=1;3=2;2=3;1=4")

anesimp$econ_ecnext_x <- recode(anesimp$econ_ecnext_x, 
                                "1=0; 2=1; 3=2; 4=3; 5=4")

anesimp$pid_x <- recode(anesimp$pid_x, 
                        "1=0; 2=1; 3=2; 4=3; 5=4; 6=5; 7=6")

anesimp$dem_edugroup_x <- recode(anesimp$dem_edugroup_x, 
                                 "1=0; 2=1; 3=2; 4=3; 5=4")

# Treat manuf as a factor variable
anesimp$manuf <-as.factor(anesimp$manuf)

# Save the dataframe as another object 
anesimpor <- anesimp 

## Feature engineering
  # treat "nationalism" as continuous
  # treat "party id" as continuous
  # treat china_econ" as factor
  # take log of Chinese M&A variables and add a small number to ensure variable do not have 0s

# Treat nationalism as continuous/numeric
anesimpor$patriot_amident <- as.numeric(anesimpor$patriot_amident)
# Treat party id as continuous 
anesimpor$pid_x <- as.numeric(anesimpor$pid_x)
# Treat china_econ as factor after recoding 
anesimpor$china_econ <- recode(anesimpor$china_econ, "1=0; 3=0; 2=1")
anesimpor$china_econ <- as.factor(anesimpor$china_econ)
# Take the log of Chinese M&A variables - add a small number as variable contains 0s
anesimpor$LogMANO <- log(anesimpor$MANo+1.01)

# summary of variables of interest
summary(anesimpor%>%select(ft_hclinton,manuf,pid_x,patriot_amident,china_econ,LogMANO))


## Modelling (with no imputation) ----------------------------------
# R will perform pairwise deletion: remove all rows that has at least one missing value for the variables in the model
# Originally, my dataset anesimpor has 5914 observations.

# linear regression model
fit_ols <-lm(ft_hclinton ~ manuf + pid_x + patriot_amident + china_econ + LogMANO, data=anesimpor)
# model summary
summary  # 1464 observations deleted due to missingness

# 1464/5914 * 100 = 24.7%
# Thus, I have to delete close to 25% of my data due to missing values.  Let's try to instead use mice
# to impute missing values so that we can retain 25% of my training sample.


# Multiple imputation with mice -----------------------------------------

# In general, it is best to impute data in its rawest form possible, 
# as any change could be derailing from its original distribution (such as creating a new variable 
# based on existing variables, or any transformation of variables).

# One exception here is the manufacturing variable I have created based on open-ended text questions. 
# I choose to create and code this variable, instead of imputing text as factor.

# With the exception of recoding and the new manuf column, I will use the anesimp as is (no feature engineering)
# as input to the MI process

# When we impute the dataset, it is important to keep the types of variables as they are, and determine
# different distributions for each variable according to their types:
  # china_econ: categorical nominal variable (binary)
  # party identification: categorical ordinal variable (0-6 scale)
  # nationalism: categorical ordinal variable (0-4 scale)

anesimp2 <- anesimp # use dataset before I perform any feature engineering

# Treat variables as factors
anesimp2$patriot_amident = as.factor(anesimp2$patriot_amident) # nationalism (ordinal variable with 0-4 scale)
anesimp2$china_econ = as.factor(anesimp2$china_econ) # china economic rise (nominal variable with 0/1 scale)
anesimp2$pid_x = as.factor(anesimp2$pid_x) # party identification (ordinal variable with 0-6 scale)

## Pattern of missing value exploration
# A dataframe of variables and their proportion of missing values
temp<-anesimp2%>%summarise_all(~sum(is.na(.))/nrow(anesimp2)) # get proportion of NA for each variable
var_names <-names(temp) # save variable names
n_missing<-as_tibble(t(as.matrix(temp))) # transpose the temp dataframe
n_missing["variables"] <-var_names # variables column
n_missing<-n_missing%>%rename("proportion.of.missing.values"="V1") %>% relocate(variables)%>%
  arrange(desc(proportion.of.missing.values)) # rename columns and sort the proportion of missing values column


# Variables such as prevote_primvwho, iwrobspre_skintone and relig_ident_1st has more than 0.25 missing values.
# It is useful to remove these variables from the dataset first as they might mess up the imputation. 
# I also remove additional variables that are highly correlated with others that stop the imputation 
# working otherwise  (however, mice also automatically detects multicollinearity and will drop one of the highly correlated
# variable.


# We have both sample_state and Statename serving for the same purpose. 
# I delete Statename variable, and turn sample_state character vector into a factor
anesimp2 <- anesimp2 %>% select(-interest_whovote2008,-prevote_primvwho, 
                -prevote_intpresst,-relig_ident_1st,-iwrobspre_skintone,
                -iwrobspre_levinfo,
                -iwrobspre_intell, -iwrobspre_interest,-gayrt_discrev_x,-Statename)

# At this step, we need to specify distributions for our to-be imputed variables and determine which variable we would like 
# to leave out of the imputation prediction process.  Note that mice will automatically detect variables
# with no missing data and mice will sliently set all predictors for that variable to zero (so no imputation 
# will be done on variables with no missing values).

imp <- mice(anesimp2, maxit=0) # run mice algorithm with 0 iterations, just so we have access to the predictorMatrix

# The Predictor Matrix (predM) informs us which variables are going to be used to predict a plausible value 
# for variables (1 means a variable is used to predict another variable, 0 otherwise). Since no variable can predict 
# itself, the intersection of one variable with itself in the matrix takes the value 0. We can manually determine if 
# we would like to leave certain variables out of prediction.
# I leave out the manufacturing variable I constructed, state indicators and all the state-level variables 

# manually leave some variables out of the predictorMatrix
predM = imp$predictorMatrix
meth = imp$method

# These variables will not be used as predictors for any variables with missing values
predM[, c("sample_state")]=0  
predM[, c("Total_mil")]=0   
predM[, c("PriOwn_mil")]=0   
predM[, c("GovValue_mil")]=0   
predM[, c("PriOwn")]=0   
predM[, c("GovOwn")]=0   
predM[, c("MANo")]=0   
predM[, c("manuf")]=0  # have missing values

head(predM)

# Notice that gender_respondent_x has NO missing value.  In this case, mice will sliently set
# the gender_repsondent_x row to zero values (so gender_repdonent_x will not be an outcome variable in the 
# imputation process)

# Specify imputation model manually for the following variables (change from the default)
meth
# ordinal categorical variable
poly_vars <- c("patriot_amident", "pid_x")
# binary variable
log_vars <- c("manuf")
# nominal categorical variable 
poly2_vars <- c("china_econ")

# set meth matrix
meth[poly_vars] = "polr"
meth[log_vars] = "logreg"
meth[poly2_vars] = "polyreg"

# As we can see above, our variables of interest are now configured to be imputed with the 
# imputation method we specified. Empty cells in the method matrix means that those variables 
# aren’t going to be imputed. Mice will automatically set variables with no missing values to "", meaning
# they won't be imputed. We can also manually set variables to not be imputed with the meth[variable]="" command.
meth

## Imputation 
  # With the mice() command, we tell mice to impute the anesimp2 data, create 5
  # "multiply imputed datasets", use predM as the predictor matrix, meth as imputation models for each variable  
  # and don't print the imputation process. If you would like to see the process, set print as TRUE
execute <- FALSE
if (execute) {
  ç <- mice(anesimp2, # dataset
               maxit = 5, # produce 5 multiply imputed datasets
               predictorMatrix = predM, # use predM as the predictorMatrix
               method = meth, # use imputation models specified in "meth" for each outcome variable in the imputation process
               print =  FALSE) # print imputation process
}


# The imputation created 5 datasets with different plausible values for missing values. 
# You can look at imputed datasets and values with the following commands:

# Look at head and tail of imputed values for china_econ variable
# (ie: the 5 columns represent each of the 5 multiply imputed datasets, the rows
# are the respondents whose missing value was imputed)
head(imp2$imp$china_econ)
tail(imp2$imp$china_econ)

# Using the complete function, I Can also extract the first multiply imputed dataset and look at the first few (head)
# rows of this dataset using the complete function
anescomp <- mice::complete(imp2, 1)  # complete(imp2, 0)  returns the original data
head(anescomp)


# Linear regression using the 5 multiply imputed datasets -------------------------------------------

# Perform OLS regression for each of the 5 multiply imputed datasets
# Pool the estimated betas together (by averaging) to get a final estimated beta.
# Get a final "corrected standard errors" that takes into account the uncertainty of the estimated beta
# across the 5 multiply imputed datasets.

# We use the "with()" function in mice

# I will aggregate the 5 multipy imputed dataset into a single dataset in long format:
# for each respondent and variable there are "5 different versions of the imputed missing value"
# notice we have id and .imp columns in anesimp_long.  .imp has values 0 to 5, where 0 is the original dataset
anesimp_long <- mice::complete(imp2, action="long", include = TRUE)  


# Convert two variables into numeric 
# For imputation, I previous convert them into factors and treat them as ordinal categorical variable.
# Now for regression, I convert them back to continuous.
anesimp_long$patriot_amident <- with(anesimp_long, 
                                     as.integer(anesimp_long$patriot_amident))
anesimp_long$pid_x <- with(anesimp_long, 
                           as.integer(anesimp_long$pid_x))

# Take log of M&A variable (do some feature engineering before regression)
anesimp_long$LogMANO<-log(anesimp_long$MANo+1.01)


# Convert from long format back to mids type - mice can perform regression modelling and pooling with this datatype
# "mids" objects stands for multiply imputed datasets objects 
anesimp_long_mids<-as.mids(anesimp_long)


# Perform regression with the "with()" function so that mice can perform automatically pooling (average beta-hat)
# and corrected standard error for beta-hat

## Regression

fit_imp <- with(anesimp_long_mids, # mids object
               lm(ft_hclinton ~ manuf + pid_x +
                    patriot_amident + china_econ + LogMANO)) # model specification

# Regression outputs
summary(pool(fit_imp))


# The pooled coefficients from the imputed datasets gave us more or less similar results as we got with the 
# listwise-deletion technique. P-values obtained from imputed datasets are also almost similar, except for one 
# variable - log of Chinese M&A (logMANO), which is now highly significant.

# This shows that multiple imputation can make a difference, but it is always useful to check, 
# re-impute, and do sensitivity analyses in order to make sure that the imputation doesn’t shed light on a false effect.



## Troubleshooting common issues with mice -----------------------------------------------------------------------

# 1.  Character vectors in dataset: Multiple imputation doesn’t deal well with character vectors in the dataset. 
# One possible solution is to delete the character vectors, but if you would like to impute them or use 
# them for a multilevel model after imputation, this solution is not practical. You can either,

  # Get rid of the character vector
  # Convert the character vector into a factor


# 2. High proportions of missing data in variables: Multiple imputation algorithms might not like to 
# include variables that have missing values in high proportions. While you are in the data exploration stage, 
# it might be useful to eliminate variables with more than 50% missing from the imputation process.


# 3. High multicollinearity: Multiple imputation doesn’t like variables that are highly correlated with each other. 
# In most cases, the mice algorithm will leave these variables out of the imputation process. However, in some cases, 
# multiple imputation might fail to start from the beginning. If the code is giving you an error, it might be useful 
# to run the imputation with only a subset of variables, and keep increasing the number of variables included until you 
# find the problematic variable. If you set print=TRUE, you will most likely see where the algorithm is having trouble 
# as it will stop working while imputing that variable.


# 4. Missing values after imputation: Always check how your variables are imputed by inpecting the imp element in 
# the mids object (For example, as we did earlier: head(imp2$imp$china_econ)). If you still see missing values after 
# imputation, this means the algorithm didn’t work as intended. There shouldn’t be huge differences between your analysis 
# pre-imputation and after-imputation, unless missing values are highly affecting your analysis (in that case, it might be 
# useful to think about other strategies to collect more data). I’d suggest you impute the whole dataset, rather than only 
# the variable of interest.

# 5. Non-missing value variables: If you have variables with no missing values, you’ll most likely have to exclude them 
# from the imputation process. This especially causes problems if your dataset is hierarchically ordered, like the one in 
# this example. All state-level predictors needed to be excluded from imputation as no values were missing from these 
# variables.



