import React, { useState } from "react";
import { api } from "../utilities";
import PropTypes from "prop-types";

const BuyStocksButton = ({ onBuySuccess }) => {
  const [ticker, setTicker] = useState("");
  const [totalShares, setTotalShares] = useState("");
  const [priceAtPurchase, setPriceAtPurchase] = useState("");
  const [dateBought, setDateBought] = useState("");

  const handleBuyStocks = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("stocks/", {
        ticker,
        total_shares: totalShares,
        price_at_purchase: priceAtPurchase,
        date_bought: dateBought,
      });
      if (response.status === 201) {
        onBuySuccess();
        window.location.reload();  // This line refreshes the entire page
      }
    } catch (error) {
      console.error("Error buying stocks:", error);
    }
  };

  return (
    <div className="w-1/4 p-8 mx-auto bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
      <h2 className="text-2xl font-bold mb-4 text-center text-[#1F2937]">Buy Stocks</h2>
      <form onSubmit={handleBuyStocks}>
        <input
          type="text"
          placeholder="Ticker"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
          className="w-full p-2 mb-4 border rounded-md"
        />
        <input
          type="number"
          placeholder="Total Shares"
          value={totalShares}
          onChange={(e) => setTotalShares(e.target.value)}
          className="w-full p-2 mb-4 border rounded-md"
        />
        <input
          type="number"
          placeholder="Price at Purchase"
          value={priceAtPurchase}
          onChange={(e) => setPriceAtPurchase(e.target.value)}
          className="w-full p-2 mb-4 border rounded-md"
        />
        <input
          type="date"
          placeholder="Date Bought"
          value={dateBought}
          onChange={(e) => setDateBought(e.target.value)}
          className="w-full p-2 mb-4 border rounded-md"
        />
        <button 
          type="submit"
          className="w-full p-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Buy Stocks
        </button>
      </form>
    </div>
  );
};

BuyStocksButton.propTypes = {
  onBuySuccess: PropTypes.func.isRequired,
};

export default BuyStocksButton;
