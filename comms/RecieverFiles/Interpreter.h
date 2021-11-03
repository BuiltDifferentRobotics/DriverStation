#pragma once

class interpreter{
  public:
  struct Data {
    // this will hold data from the controller
    int front_left_;
    int front_right_;
    int back_left_;
    int back_right_;
    Data(int a, int b, int c, int d)
      : front_left_(a), front_right_(b), back_left_(c), back_right_(d) {}
  }
  void run(); // forever running
  private:  
  int port;
  Data parseInput();
};