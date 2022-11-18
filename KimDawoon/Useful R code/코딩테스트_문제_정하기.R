### load library
library(dplyr)

### participate
random_question <- function(parti, cf = c()){
  
  # message
  cat("바쁜 인원 : ", cf, "\n")
  
  # select main person
  restpeople <- setdiff(parti,cf)
  
  num <- sample(c(floor(length(restpeople)/2),ceiling(length(restpeople)/2)),1)
  
  q1 <- sample(restpeople,num)
  q2 <- setdiff(restpeople,q1)
  
  # select conform person
  num2 <- sample(c(floor(length(cf)/2),ceiling(length(cf)/2)),1)
  
  cq1 <- sample(cf,num2)
  cq2 <- setdiff(cf,cq1)
  
  cat("첫번째 문제 : 연산자 끼워 넣기 \n해당하는 사람 :", c(q1,cq1) ,"\n두번째 문제 : 인구 이동 \n해당하는 사람 :",c(q2,cq2))
}

random_question(c("지우","동현","시현","나린","다운"), c("나린"))