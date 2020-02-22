package trainer

import (
  "math/rand"
  "time"
)

type trainer struct {
  name string
  gender string
  has_pokedex bool
  secret_id int
  trainer_id int
  final_id int
}

func NewTrainer(n, g string) *trainer {
  rand.Seed(time.Now().UnixNano())
  var s_id int = rand.Intn(99999 - 0 + 1) + 0
  var t_id int = rand.Intn(65535 - 0 + 1) + 0
  var f_id int = t_id + s_id * 65536

  t := trainer{n, g, false, s_id, t_id, f_id}
  return &t
}
