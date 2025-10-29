// pricer_main.cpp - example CLI for OptionsPricer
#include "OptionsPricer.hpp"
#include <iostream>

int main() {
  double S = 100.0;
  double r = 0.01;
  double sigma = 0.2;
  double t = 0.5; // half year
  std::vector<double> strikes = {80, 90, 100, 110, 120};

  auto prices = qmul::options::price_calls(strikes, S, r, sigma, t);
  std::cout << "Strikes -> Call prices\n";
  for (size_t i = 0; i < strikes.size(); ++i) {
    std::cout << strikes[i] << " -> " << prices[i] << "\n";
  }
  return 0;
}
