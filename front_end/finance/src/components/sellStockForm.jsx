import React, { useState } from "react";
import { api } from "../utilities";

const SellStocksForm = ({ stockId, onSellSuccess }) => {
  const [numberOfShares, setNumberOfShares] = useState("");
  const [sellDate, setSellDate] = useState("");
  const [sellPrice, setSellPrice] = useState("");

  const handleSell = async () => {
    try {
      const response = await api.post(`stocks-sales/sell-stock/${stockId}/`, {
        sold_shares: parseFloat(numberOfShares),
        sell_date: sellDate,
        sell_price: parseFloat(sellPrice),
      });

      console.log("Stock sold successfully:", response.data);

      // Reset form inputs
      setNumberOfShares("");
      setSellDate("");
      setSellPrice("");

      // Notify the parent component about the successful sale
      if(onSellSuccess) {
        onSellSuccess();
      }
      
    } catch (error) {
      console.error("Error selling stocks:", error);
    }
  };

  return (
    <div className="flex justify-center bg-[#1F2937]">
        <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md w-96 mt-8">
            <h2 className="text-2xl font-bold mb-4 text-center text-white">Sell Stocks</h2>

            <input
                type="number"
                placeholder="Number of Shares"
                value={numberOfShares}
                onChange={(e) => setNumberOfShares(e.target.value)}
                className="w-full p-2 mb-4 border rounded-md"
            />

            <input
                type="date"
                placeholder="Sell Date"
                value={sellDate}
                onChange={(e) => setSellDate(e.target.value)}
                className="w-full p-2 mb-4 border rounded-md"
            />

            <input
                type="number"
                placeholder="Sell Price"
                value={sellPrice}
                onChange={(e) => setSellPrice(e.target.value)}
                className="w-full p-2 mb-4 border rounded-md"
            />

            <button 
                onClick={handleSell} 
                className="w-full p-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
                Sell
            </button>
        </div>
    </div>
  );
};

export default SellStocksForm;
