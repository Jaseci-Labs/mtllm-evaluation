import:py from jaclang.core.llms, OpenAI;
import:py from PIL, Image;

glob llm = OpenAI(model_name="gpt-4o");

obj PurchasedItem {
    has name: str, price: float, quantity: int;
}

obj Receipt {
    has store: 'Store Name': str,
        date: 'Purchase Date': str,
        items: list[PurchasedItem],
        total: float;

    can pp() -> None {
        print(f"Store: {self.store}");
        print(f"Date: {self.date}");
        for item in self.items {
            print(f"{item.name} x {item.quantity} = {item.price}");
        }
        print(f"Total: {self.total}");
    }
}

can get_reciept(reciept_img: Image) -> Receipt by llm();

with entry {
    reciept_img = Image.open("receipt.jpg");
    receipt = get_reciept(reciept_img);
    receipt.pp();
}