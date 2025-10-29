// OptionsPricer.hpp - simple option pricing utilities
#pragma once

#include <vector>

namespace qmul {
namespace options {

// Simple Black-Scholes European option pricer (calls only)
// S: spot price, K: strike, r: risk-free rate, sigma: volatility, t: time to
// expiry (years)
double black_scholes_call(double S, double K, double r, double sigma, double t);

// Calculate option prices for a vector of strikes
std::vector<double> price_calls(const std::vector<double> &strikes, double S,
                                double r, double sigma, double t);

} // namespace options
} // namespace qmul
