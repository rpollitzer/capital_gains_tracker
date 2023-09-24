import React, { useEffect, useState } from 'react';
import { api } from '../utilities';
import SellStocksForm from './SellStocksForm';

const StockSalesTable = () => {
  const [stockSalesData, setStockSalesData] = useState([]);
  const [selectedStockId, setSelectedStockId] = useState(null);

  const fetchStockSales = async () => {
    try {
      let token = localStorage.getItem('token');
      if (token) {
        api.defaults.headers.common['Authorization'] = `Token ${token}`;
        const response = await api.get('stocks/');
        setStockSalesData(response.data);
      }
    } catch (error) {
      console.error('Error fetching stock sales data:', error);
    }
  };

  useEffect(() => {
    fetchStockSales();
  }, []);

  const handleSellStock = (stockId) => {
    setSelectedStockId(stockId); 
  };

  return (
    <div className="w-2/4 p-8 mx-auto bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <h5 class="mb-3 text-3xl font-bold tracking-tight text-center text-gray-900 dark:text-white">Stock Holdings</h5>
        <table class="mx-auto">
            <thead>
                <tr class="mb-3 font-medium text-gray-700 dark:text-gray-400">
                    <th class="text-center align-middle px-4">Date Bought</th>
                    <th class="text-center align-middle px-4">Ticker</th>
                    <th class="text-center align-middle px-4">Total Shares</th>
                    <th class="text-center align-middle px-4">Price at Purchase</th>
                    <th class="text-center align-middle px-4">Total Invested</th>
                    <th class="text-center align-middle px-4">Action</th>
                </tr>
            </thead>
            <tbody>
                {stockSalesData.length === 0 ? (
                    <tr>
                        <td class="text-white text-center align-middle px-4" colSpan="6">No data exist</td>
                    </tr>
                ) : (
                    stockSalesData.map((sale, index) => (
                        <tr key={index}>
                            <td class="text-white text-center align-middle px-4">{sale.date_bought}</td>
                            <td class="text-white text-center align-middle px-4">{sale.ticker}</td>
                            <td class="text-white text-center align-middle px-4">{sale.total_shares}</td>
                            <td class="text-white text-center align-middle px-4">${sale.price_at_purchase}</td>
                            <td class="text-white text-center align-middle px-4">${sale.total_shares * sale.price_at_purchase}</td>
                            <td class="text-center align-middle px-4">
                                <button class='inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800' onClick={() => handleSellStock(sale.id)}>Sell</button>
                            </td>
                        </tr>
                    ))
                )}
            </tbody>
        </table>
        {selectedStockId !== null && (
            <SellStocksForm
                stockId={selectedStockId}
                onSellSuccess={() => {
                    setSelectedStockId(null); 
                    fetchStockSales(); // Refetch the stocks data upon successful sell operation
                }}
            />
        )}
    </div>
  );
};

export default StockSalesTable;
