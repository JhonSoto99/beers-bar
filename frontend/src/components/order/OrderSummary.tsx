"use client";

import { getOrderSummary } from "app/services/beers-bar-backend";
import { OrderDetails } from "app/components/order/OrderDetails";
import { ItemList } from "app/components/order/ItemList";
import { RoundList } from "app/components/order/RoundList";
import { Order } from "app/app/types";
import { useEffect, useState } from "react";
import { Loader } from "app/components/shared/Loader";
import { Error } from "app/components/shared/Error";

export const OrderSummary = () => {
  const [orderSummary, setOrderSummary] = useState<Order | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchOrderSummary = async () => {
      try {
        const data: Order = await getOrderSummary();
        setOrderSummary(data);
      } catch {
        setError("Failed to fetch order summary");
      } finally {
        setLoading(false);
      }
    };

    fetchOrderSummary();
  }, []);

  if (loading) return <Loader />;
  if (error) return <Error error={error} />;
  if (!orderSummary) return <p>No order summary available.</p>;

  return (
    <section className="p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-10">
      <h1 className="text-3xl font-bold text-center mb-6">Order Summary</h1>

      <OrderDetails
        subtotal={orderSummary.subtotal}
        taxes={orderSummary.taxes}
        discounts={orderSummary.discounts}
        paid={orderSummary.paid}
      />

      <ItemList items={orderSummary.items} />
      <RoundList rounds={orderSummary.rounds} />
    </section>
  );
};
