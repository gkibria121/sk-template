const j1 = [
  {"item": "apple", "price": 10},
  {"item": "mobile", "price": 30},
];
const j2 = [
  {"item": "apple", "quantity": 30},
  {"item": "apple", "quantity": 20},
  {"item": "mobile", "quantity": 40},
];

const cost = [];
for (const item of j1) {
  const item2 = j2.find((i) => i.item === item.item);
  console.log(item2);
  if (item2) {
    const costItem = {
      "item": item.item,
      "cost": item.price * item2.quantity,
    };
    cost.push(costItem);
  }
}

const json = JSON.stringify(cost, null, 2);
console.log(json);
