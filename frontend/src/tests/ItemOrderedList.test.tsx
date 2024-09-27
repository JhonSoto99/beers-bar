import { render, screen } from "@testing-library/react";
import { ItemOrderedList } from "app/components/order/ItemOrderedList";
import { ItemOrdered } from "app/app/types";

describe("ItemOrderedList Component", () => {
  it("renders items correctly", () => {
    const items: ItemOrdered[] = [
      { name: "Item 1", quantity: 2 },
      { name: "Item 2", quantity: 3 },
    ];

    render(<ItemOrderedList items={items} />);

    expect(screen.getByText("Items Ordered")).toBeInTheDocument();
    expect(screen.getByText("Item 1")).toBeInTheDocument();
    expect(screen.getByText("Cantidad: 2")).toBeInTheDocument();
    expect(screen.getByText("Item 2")).toBeInTheDocument();
    expect(screen.getByText("Cantidad: 3")).toBeInTheDocument();
  });

  it("renders nothing if items array is empty", () => {
    render(<ItemOrderedList items={[]} />);

    expect(screen.getByText("Items Ordered")).toBeInTheDocument();
    expect(screen.queryByText("Item 1")).not.toBeInTheDocument();
    expect(screen.queryByText("Item 2")).not.toBeInTheDocument();
  });
});
