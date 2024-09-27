import { render, screen } from "@testing-library/react";
import { OrderDetails } from "app/components/order/OrderDetails";
import { OrderDetailsProps } from "app/app/types";

describe("OrderDetails Component", () => {
  const props: OrderDetailsProps = {
    subtotal: 100,
    taxes: 15,
    discounts: 10,
    paid: true,
  };

  it("renders order details correctly", () => {
    render(<OrderDetails {...props} />);

    expect(screen.getByText(/Subtotal:/)).toHaveTextContent("$100");
    expect(screen.getByText(/Taxes:/)).toHaveTextContent("$15");
    expect(screen.getByText(/Discounts:/)).toHaveTextContent("$10");
    expect(screen.getByText(/Status:/)).toHaveTextContent("Paid");
  });

  it("renders pending status correctly", () => {
    const pendingProps: OrderDetailsProps = {
      subtotal: 100,
      taxes: 15,
      discounts: 10,
      paid: false,
    };

    render(<OrderDetails {...pendingProps} />);
    expect(screen.getByText(/Status:/)).toHaveTextContent("Pending");
  });
});
