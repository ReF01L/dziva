let value_items = [];

(() => {
    document.querySelectorAll('.stepper-value').forEach(item => {
        item.innerText = '1';
        value_items.push({el: item, count: 1})
    });
})()

const step = (event, add = true) => {
    let sender = event.target || event.srcElement
    let product_id = parseInt(sender.parentElement.id.match(/\d+/));
    let elem = document.querySelector(`#counter-${product_id}`);
    let index = value_items.map(item => item.el).indexOf(elem)
    if (add) {
        if (value_items[index].count < 50)
            value_items[index].count++;
    }
    else {
        if (value_items[index].count > 1)
            value_items[index].count--;
    }
    elem.innerText = value_items[index].count;
}