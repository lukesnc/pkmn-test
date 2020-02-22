package main

import (
  "fmt"
  //"../../internal/pkmnbase"
  //"../../internal/stats"
  "../../internal/trainer"
)

func main() {
  me := trainer.NewTrainer("Luke", "M")
  fmt.Println(me)
}
