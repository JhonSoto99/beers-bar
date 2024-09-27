import { OrderDetailsProps } from "app/app/types";

export const OrderDetails = ({
  subtotal,
  taxes,
  discounts,
  paid,
}: OrderDetailsProps) => {
  return (
    <section className="mb-6">
      <div className="text-center space-y-2 text-gray-600">
        <p>
          Subtotal: <span className="font-medium">${subtotal}</span>
        </p>
        <p>
          Taxes: <span className="font-medium">${taxes}</span>
        </p>
        <p>
          Discounts: <span className="font-medium">${discounts}</span>
        </p>
        <p>
          Status:{" "}
          <span className={paid ? "text-green-500" : "text-red-500"}>
            {paid ? "Paid" : "Pending"}
          </span>
        </p>
      </div>
    </section>
  );
};
