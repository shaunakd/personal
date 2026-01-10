#ifndef BLACKSCHOLESMODEL_HPP
#define BLACKSCHOLESMODEL_HPP

struct MarketData {
    double r; // interest rate
    double S; // share price
    double q; // dividend yield
    double sigma; // volatility
};

struct TradeData {
    double K; // strike price
    double N; // notional
    double T; // years to expiry
};

#endif
