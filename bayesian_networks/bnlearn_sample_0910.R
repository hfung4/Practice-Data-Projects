# This code replicates the Bayesian Network Example with the bnlearn package
# Ref: https://www.r-bloggers.com/bayesian-network-example-with-the-bnlearn-package/

# BN have a structure that specifies the realtionship between variables.
# The strength of each relationship is given by conditional probabiltiies (CPTs).

# Build BN using the AIS dataset from the DAAG package.
# Dataset is sued to determine if there was difference in hemoglobin levels (DV) for
# different sports disciplines (features).

library(DAAG)
library(ggplot2)
library(bnlearn)
library(visNetwork)

# Get ais dataset from DAAG
data(ais)

# Explore data
dim(ais)
head(ais)
str(ais)
colnames(ais)

# Plot different distributions of hemoglobin levels for different sports
ggplot(ais, # dataframe
       aes(x=sport, # type of sports
           y= hg)) +  # homoglobin level
       geom_boxplot()

# Different sports seem to have different average homoglobin level, 
# so sports might have some effect on hg.



###### Discrete Case #######

# Build a BN with 3 Rvs:
  # hc: volume percentage of red bllod cells in bookd.
  # sports: type of sports
  # hg: level of homoglibin concentration

# Convert hg and hc (continuous variables) to binary variables and
# take only 3 levels in sports: netball, tennis, and waterpolo.

ais$high_hc <- as.factor(ais$hc > median(ais$hc))
ais$high_hg <- as.factor(ais$hg > median(ais$hg))

levels(ais$high_hc)
levels(ais$high_hg)

# create an empty graph
structure <- empty.graph(c("high_hc", "high_hg", "sport"))

# The format of the model strings is as follows. The local structure of each node 
# is enclosed in square brackets ("[]"); 
# the first string is the label of that node. The parents of the node (if any) 
# are listed after a ("|") and separated by colons (":"). 
# All nodes (including isolated and root nodes) must be listed.

# set relationships amongst to RVs manually
modelstring(structure) <- "[high_hc][sport][high_hg|sport:high_hc]"

# Plot BN using visNetwork Package
# Function for plotting
plot_network <- function(structure, ht="400px"){
  nodes_uniq <- unique(c(structure$arcs[,1],
                         structure$arcs[,2]))
  # define nodes and edges
  
  nodes <- data.frame(id = nodes_uniq,
                      label = nodes_uniq,
                      color = "darkturquoise",
                      shadow = TRUE)
  
  edges <- data.frame(from = structure$arcs[,1], # from nodes in the 'from' col
                      to = structure$arcs[,2], # to nodes in the 'to' col
                      arrows = "to",
                      smooth = TRUE,
                      shadow = TRUE,
                      color = "black")
  
  return(visNetwork(nodes, edges, height = ht, width = "100%"))
  
}


# Plot structure
# We explicit specify the relationships between the three RV

# Manually creating the structure is often a good way to go 
# since you are required to understand the system you are trying to model 
# and not relying on a black box to do it for you. 
plot_network(structure)

# The DAG is telling us that:
  # hg are conditionally dependent on gc and sport.
  # Sport and hc are marginally independent.
  # Sport and hc are dependent conditional on hg.


# Armed with the user-specified BN (nodes, edges, and direction),
# I can compute the conditional probabilities (strength of relationship)
# implied by the model and data  (what cond. prob I must have given the data
# and assuming the structure of BN is "true".)

ais_subset <- ais[ais$sport %in% c("Netball", "Tennis", "W_Polo"), 
                  c("high_hc", "high_hg", "sport")]

colnames(ais_subset)

ais_subset$sport <- factor(ais_subset$sport) # turn sport into factor var

bn_mod <- bn.fit(structure, data = ais_subset) # fit data to BN

# Get summary of the parameters of the BN, basically it contains 
# the CPT of each node
bn_mod 

# cat() concat text and objects
# cpquery() performs conditional probability queries
# It estimates the conditional probability of an event, conditional on evidence.
# Below I have: probability of high hg = True, given no evidence (so I have marg prob)
# bn_learn uses causal inference algorithms to compute this probability.
("P(high hemaglobin levels) =", 
    cpquery(bn_mod, (high_hg=="TRUE"), debug=TRUE), "\n")


cat("P(high hemaglobin levels | play water polo and have high hematocrit ratio) =", 
    cpquery(bn_mod, (high_hg=="TRUE"), (sport == "W_Polo" & high_hc == "TRUE")), "\n")

# Unlike regression models where explanatory variables are "fixed", they are not 
# fixed for BNs.  Some node can be made the "subject of query" for the inference.
# We can use the same BN to query the probability that an athlete plays
# Water Polo given we observe high hg, or the probability of having high hg
# given that the atheletes play water polo.


cat("P(they play water polo | high hemaglobin levels and have high hematocrit ratio) =", 
    cpquery(bn_mod, (sport=="W_Polo"), (high_hg == "TRUE" & high_hc == "TRUE")), "\n")


# If we don't know hc levels, we can still query P(high hg =1 |Water polo),
# We need to sum over the hc probability distribution, which cpquery does for us


cat("P(high hemaglobin levels | play water polo) =", 
    cpquery(bn_mod, (high_hg=="TRUE"), (sport == "W_Polo")), "\n")



###### Continuous Case #######

# We can also include continuous in the BN. Instead of probability
# distribution functions, we estimate probability density functions.

# Again, we start with an empty graph. I specify three RVs in the graph
structure <- empty.graph(c("hc","hg","sport"))

# I specify the causal relationships between the RVs manually (nodes, edges and 
# direction of the edges)
modelstring(structure) <-"[hc][sport][hg|sport:hc]"

# Again I take subset of ais data (only take 3 sports: Netball, Tennis, W_POlo)
# However, instead of discretizing the continuous variables hg and hc into hi/low,
# we will use them as is.

ais_sub <- ais[ais$sport %in% c('Netball','Tennis','W_Polo'), # rows
               c('hc','hg','sport')] # columns

ais_sub$sport <- factor(ais_sub$sport)

# fit data to BN to estimate the CPTs for each node
bn_mod<-bn.fit(structure, data=ais_sub)
bn_mod  



# When querying from the bn, we need to specify a range since 
# we are dealing with pdfs now

cat("P(hemaglobin levels >14 | play water polo and hc>42 =",
    cpquery(bn_mod, event = (hg>14), evidence = (sport == "W_Polo" &
                                                   hc>42)),"\n")



######## Chained Relationships (causal chains) #############

# Nodes can be chained together: lbm causes hc, both hc and sport causes hg
# I can infer the causal effect of lbm (root cause) on hg (final outcome)

# lbm: lean body mass, compute by body weight (kg) - body fat (kg)
# The higher the number, the leaner the athelete.

# Create the empty graph, now I specify an additional RV: lbm
structure <- empty.graph(c("hc","hg","sport","lbm"))

# Set the causal relationship (BN) manually.
modelstring(structure) <-"[lbm][hc|lbm][sport][hg|sport:hc]"

# visualize the BN using my plot_network function
plot_network(structure)

# fit data to BN

# As before, only take 3 sports.  I will use the continuous variables
# hg, hc, and lbm
ais_sub<- ais[ais$sport %in% c("Netball", "Tennis", "W_Polo"),
              c("hc","hg","sport","lbm")]
ais_sub$sport <-factor(ais_sub$sport)

bn_mod<-bn.fit(structure,data=ais_sub)

bn_mod

# Conditional probability queries from the trained BN
cat("P(hg >14|play Water polo, LBM>65kg)=",
     cpquery(bn_mod, event = (hg>14), evidence=(sport=="W_Polo" & lbm>65)),"\n")


# I can use causal discovery algorithms to learn the BN 
# based on observed conditional probabilities from the data rather
# than specifying the BN (edges between nodes, direction of edges) manually.

# I can also do both: ask bnlearn to perform causal discovery, then add
# addition edges to the BN based on domain knowledge.

# bnlearn uses a causal discovery algorithm called "hill climbing".
# It optimizes the model with BIC as the default metric.


# Learn the BN structure using the Hill Climbing Algorithm and BIC as 
# performance metric.
# NOTE: hc(.) is the Hill Climbing Algorithm in bnlearn
structure <- hc(ais_sub, score = "bic-cg")
plot_network(structure) # plot the structure I got from causal discovery

# This structure is different than the one we manually specified.
# This structure "best fits" the data and yields the highest BIC.
# If we have very complex system, we might need to rely on causal discovery 
# more as we don't have a very good prior knowledge about the causal structure
# and direction of the system.

# Fit data to the BN
bn_mod <- bn.fit(structure, data=ais_sub)
cat("P(hg>14 |play Water Polo, lbm>65kg)=",
    cpquery(bn_mod, event=(hg>14),
            evidence= (sport=="W_Polo" & lbm>65)),"\n")


#### Full model with ALL RVs in the dataset ######

ais_full <- ais[, c("hc", "hg", "sport", "lbm", "rcc", "wcc", "ferr", 
                   "ht", "wt", "sex", "ssf")]

# Use hill climbing to find BN struct
structure <- hc(ais_full, score = "bic-cg") 

bn_mod <- bn.fit(structure, data = ais_full)

plot_network(structure, ht = "600px")


## Use cases

# Fitting the network and querying the model is only the first 
# part of the practice. Where Bayes nets really shine is how 
# they are used to make actionable decisions. 

# we fit a model to help explain the influencing factors on 
# hemoglobin concentration in an athlete.

# hg levels might in turn affect performance.  To maintain high hg levels
# the athelete might "intervene" and do things like chainging diet, training,
# and rest.

# It is when 'interventions' such as these can be accounted for 
# in the model the user can implement 'what if' scenarios to 
# help make the best decision.


# The outputs of a Bayesian network are conditional probabilities. 
# Often these are used as input for an overarching optimisation problem. 
# For example an insurance company may construct a Bayesian network to 
# predict the probability of signing up a new customer to premium plan 
# for the next marketing campaign. 
# This probability is then used to calculate the expected 
# revenue from new sales