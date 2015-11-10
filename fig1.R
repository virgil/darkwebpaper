#library(jsonlite)
library(ggplot2)
setwd('/g/darkwebpaper/')
require(grDevices)

#data <- fromJSON(file="fig3.json")


data <- data.frame(read.csv(file="fig1.csv", col.names=c("h","reqs","traffic")) )

# convert all to percentages
data$reqs <- (data$reqs / sum(data$reqs)) * 100
data$traffic <- (data$traffic / sum(data$traffic)) * 100

#attach(data)
LAST_RANK <- 1000
s_reqs <- sort(data$reqs, decreasing=TRUE)[1:LAST_RANK]
s_traffic <- sort(data$traffic, decreasing=TRUE)[1:LAST_RANK]

################################################################################
# Plot of the %-requests rank
pdf("figs/fig3a.pdf")
plot(1:length(s_traffic), log10(s_traffic), xlab='', ylab='', yaxt='n', col='black' )
points(1:length(s_reqs), log10(s_reqs), xlab='', ylab='', yaxt='n', col='blue' )
title( xlab="Domain Rank", ylab="Percentage", main="Requests/Traffic by domain" )
axis(2, at=c(-4,-3,-2,-1,0,1), c('.0001%','.001%','.01%','.1%','1%','10%'), las=1 )
legend( 700, 1.0, c("% Requests", "% Traffic"), col=c('blue','black'), lwd=c(3,3) )
dev.off()
################################################################################



################################################################################
# Plot of the % ranks in log-log
pdf("figs/fig3b.pdf")
plot( log10(1:length(s_traffic)), log10(s_traffic), xlab='', ylab='', yaxt='n', xaxt='n', col='black', lwd=2 )
points( log10(1:length(s_reqs)), log10(s_reqs), xlab='', ylab='', yaxt='n', col='blue', lwd=2 )

title( xlab="Domain Rank", ylab="Percentage", main="Requests/Traffic by domain" )
axis(1, at=c(0,0.5,1,1.5,2,2.5,3), c('1','3','10','132','100','316','1000'), las=1 )
axis(2, at=c(-4,-3,-2,-1,0,1), c('.0001%','.001%','.01%','.1%','1%','10%'), las=1 )
legend( 0, -3, c("% Requests", "% Traffic"), col=c('blue','black'), lwd=c(3,3) )
dev.off()
################################################################################

