library(ggplot2)
setwd('/g/darkwebpaper/')
#require(grDevices)
library(plyr)
library(RColorBrewer)

data <- data.frame(read.csv(file="fig3.csv", col.names=c("cn","reqs","traffic")) )

# remove some countries from consideration
# 98: Europe, 107: Anonymous Proxy
data <- data[-c(98,107), ]

# convert all to percentages
data$reqs <- (data$reqs / sum(data$reqs)) * 100
data$traffic <- (data$traffic / sum(data$traffic)) * 100

LAST_RANK <- 8

cbPalette <- c(rainbow(LAST_RANK-1,s=1.0,v=0.8), "#56B4E9", "#009E73","#333333" )
               
# "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#CC6666", "#9999CC", "#66CC99", "#333333")

# sort by reqs, get top LAST_RANK.  Drop uneeded column.  Add the "Other" row
data_reqs <- (data[ with(data, order(-reqs)), ])[1:LAST_RANK,]
data_reqs <- data_reqs[c('cn','reqs')]

percent_other_reqs <- 100.0 - sum(data_reqs$reqs)
data_reqs <- rbind(data_reqs, data.frame(cn='Other',reqs=percent_other_reqs) )
data_reqs$type <- '% Requests'

# sort by traffic, get top LAST_RANK. Drop uneeded column. Add the "Other" row
data_traf <- (data[ with(data, order(-traffic)), ])[1:LAST_RANK,]
data_traf <- data_traf[c('cn','traffic')]

percent_other_traffic <- 100.0 - sum(data_traf$traffic)
data_traf <- rbind(data_traf, data.frame(cn='Other',traffic=percent_other_traffic) )
data_traf$type <- '% Traffic'

# merge the data together
data_reqs <- rename(data_reqs, c("reqs"="percentage"))
data_traf <- rename(data_traf, c("traffic"="percentage"))
mdata <- rbind( data_reqs, data_traf )



################################################################################
# Plot the basic frame of the stacked bar chart.

#aes(x=reorder(category, -ips)

pdf("figs/fig3.pdf")
p <- ggplot(data = mdata, aes(y = percentage, x=type, order=-percentage, fill=cn) )
p <- p + geom_bar(stat = "identity") + ggtitle("Top Countries") + xlab('') + labs(fill='')

p <- p + scale_y_continuous(breaks=c(0,25,50,75,100), labels=c('0', '25%','50%','75%','100%') )

# To use for fills, add
p + scale_fill_manual(values=cbPalette)  + scale_colour_manual(values=cbPalette)

dev.off()

