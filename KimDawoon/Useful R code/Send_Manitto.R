### load library
library(sendmailR)
library(dplyr)
library(Microsoft365R)

### ms365
my_outlook <- get_personal_outlook()

### select manitto
manitto <- function(member = c(), to = c()){
  a <- 1:length(member)
  b <- a
  while(any(a==b)){
    b <- sample(a,length(member))
  }
  for(i in 1:length(member)){
    to2 <- to[i]
    my_email <- my_outlook$create_email(content_type = "html")$
    set_body(paste0("<p>Thank you",member[a[i]],"for Sihyeon's manitto games!</p>
                    <p>It's your manitto member :</p>",
                    member[b[i]],
                    "<p>U will take the present under 10,000won price.</p>
                    <p>Ok. Good Luck</p>"))$
    #set_subject("Manitto Result")$
    set_subject("Manitto Results")$
    set_recipients(to=to2)
    
    my_email$send()
  }
}

### member's email
setwd("/Users/ybm/desktop")
memberlist <- read.csv("betatest.csv",header=T)

### send
manitto(memberlist$name,memberlist$email)
