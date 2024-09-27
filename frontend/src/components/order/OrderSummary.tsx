import { getOrderSummary } from "app/services/beers-bar-backend";
import { OrderDetails } from "app/components/order/OrderDetails";
import { ItemList } from "app/components/order/ItemList";
import { RoundList } from "app/components/order/RoundList";
import { Order } from "app/app/types";

export const OrderSummary = async () => {
  const orderSummary: Order = await getOrderSummary();

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
