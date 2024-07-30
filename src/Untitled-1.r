num <- readline(prompt="Enter a number: ")
num <- as.integer(num)
if (is.na(num)) {
  print("Invalid input. Please enter a valid integer.")
} else {
  sum <- 0
  temp <- num
 
  while(temp > 0) {
    digit <- temp %% 10
    sum <- sum + (digit ^ 3)
    temp <- floor(temp / 10)
  }
 
  if(num == sum) {
    print(paste(num, "is an Armstrong number"))
  } else {
    print(paste(num, "is not an Armstrong number"))
  }
}
