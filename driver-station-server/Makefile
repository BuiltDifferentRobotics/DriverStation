server: main.o
	g++ main.o -o server

main.o: main.cpp
	g++ -c main.cpp


test: test.o
	g++ test.o -o test

test.o: test.cpp
	g++ -c test.cpp


clean: 
	rm -rf *.o test server
