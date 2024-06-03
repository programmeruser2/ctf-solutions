package main 
import (
    "testing"
)
func run(code []byte) {
    vm := NewVM()
    vm.launch(code)
}
func FuzzPppvm(f* testing.F) {
    f.add([]byte(""));
    f.Fuzz()
}



