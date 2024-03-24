export default function updateUniqueItems(groceryList) {
    // returns a map with updated map items.
    //changes 'rice' => 1 to 'rice' => 100.
   //if not a map return Cannot process
  
    if (groceryList instanceof Map) {  
      for (let product of groceryList) {
        if (product[1] === 1) 
          groceryList.set(product[0], 100);
      }
      return groceryList;
     }
    else {
      console.log('Cannot Process');
   }
  }