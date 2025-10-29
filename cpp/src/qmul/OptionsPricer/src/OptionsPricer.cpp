// OptionsPricer.cpp - minimal Black-Scholes implementation

#include "OptionsPricer.hpp"
#include <cmath>

namespace qmul {
namespace options {

// Cumulative distribution function for standard normal
static double norm_cdf(double x) {
  return 0.5 * std::erfc(-x / std::sqrt(2.0));
}

double black_scholes_call(double S, double K, double r, double sigma,
                          double t) {
  if (t <= 0.0)
    return std::max(0.0, S - K);
  if (sigma <= 0.0)
    return std::max(0.0, S * std::exp(-r * t) - K);
  double d1 = (std::log(S / K) + (r + 0.5 * sigma * sigma) * t) /
              (sigma * std::sqrt(t));
  double d2 = d1 - sigma * std::sqrt(t);
  return S * norm_cdf(d1) - K * std::exp(-r * t) * norm_cdf(d2);
}

std::vector<double> price_calls(const std::vector<double> &strikes, double S,
                                double r, double sigma, double t) {
  std::vector<double> out;
  out.reserve(strikes.size());
  for (double K : strikes) {
    out.push_back(black_scholes_call(S, K, r, sigma, t));
  }
  return out;
}

} // namespace options
} // namespace qmul
