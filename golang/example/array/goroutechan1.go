package main

import (
	"fmt"
	"math/rand"
	"time"

//"strconv"
)

type recv struct {
	data string
	size int
}

func webserver(num int, c chan recv, d chan recv) {
	//fmt.Println(num)
	var data recv
	for {
		fmt.Println("server", num)
		r := rand.Intn(10)
		data.size = num
		data.data = "bbb"
		if r%2 == 0 {
			data.data = "aaa"
		}
		time.Sleep(time.Second * time.Duration(r))
		if r%2 == 0 {
			c <- data
		} else {
			d <- data
		}
	}

}
func workerqueue(num int, c chan recv, d chan recv) {
	//fmt.Println(num)
	for {
		select {
		case msg := <-c:
			fmt.Println("aaa", msg.size, msg.data)
		case msg := <-d:
			fmt.Println("bbb", msg.size, msg.data)
		}
	}

}

func main() {
	c := make(chan recv)
	d := make(chan recv)
	go webserver(1, c, d)
	go webserver(2, c, d)
	go workerqueue(2, c, d)
	go workerqueue(3, c, d)
	var input string
	fmt.Scanln(&input)

}
