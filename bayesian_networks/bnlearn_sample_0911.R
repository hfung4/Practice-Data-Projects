# This script reproduces the example in R-bloggers on the usuage
# of bnlearn.  I have added my own notes also.
# REF: https://www.r-bloggers.com/bayesian-network-in-r-introduction/

library(bnlearn)

data(coronary)

dim(coronary)
colnames(coronary)
str(coronary)

# Causal discoery to learn the BN structure using the Hill Climbing algorithm
bn_df = data.frame(coronary)
res = hc(bn_df)

plot(res)

# The hc algorithm comes up with the follow causal structure that fits the
# data most closely (based on some performance metric).
# The DAG implies certain conditional dependences/independences between variables.

# Some of the causality between some nodes is intuitive; however others are not.
# For example, how come family history of the coronary heart disease
# is dependent on having strenuous mental work?

# Let's remove the arc (aka: edge or link) between family and M.Work
res$arcs = res$arcs[-which((res$arcs[,'from']=="M..Work" & 
                              res$arcs[,'to']=="Family")),]


plot(res)


# Now that we have the BN structure (arcs and direction of arcs), we can 
# find out the strength of the relationships, given by CPTs at each node.
# I infer this strength of relationship using the observed data and
# the causal structure.

# train the bn
fitted_bn = bn.fit(res, data= bn_df)

fitted_bn


# To see the CPT of a specific node, do the following:
# Protein is conditioned on M.Work and Smoking. Since both of these 
# variables are binary variables (only two values) the CPT table 
# has 2×2=4 entries
print(fitted_bn$Proteins)



# Inference: I can make conditional probability queries from the fitted BN

# Infer from the fitted BN: P(Proteins <3 | Smoking == no)
cpquery(fitted_bn, event = (Proteins=="<3"), evidence = ( Smoking=="no") )


# We can also move in the opposite direction of an arc between two nodes. 
# Let's see if a person's Proteins level is greater than 3, then 
# what is the chance that his or her Pressure level is greater than 140?

# P(Pressure >140 | Proteins <3)
cpquery(fitted_bn, event = (Pressure==">140"), evidence = ( Proteins=="<3" ) )
