(() => {
    titles = Array.from(document.querySelectorAll('.product__content__body__main__header-title'))
    let frames = Array.from(document.querySelectorAll('.product__content__body__main__content'))
    
    titles.forEach((element, i) => {
        element.addEventListener('click', () => {
            let active_el = document.querySelector('.product__content__body__main__header-title.active')
            let active_frame = document.querySelector('.product__content__body__main__content.active')

            if (active_el != element) {
                element.classList.add('active')
                let frame = frames[i]
                frame.classList.add('active')
                frame.style.transform = `translateY(${-i * 100}%)`

                active_el.classList.remove('active')
                active_frame.classList.remove('active')
                shift_down(active_frame, frames.indexOf(active_frame))
            }
        })
    });
    frames[2].style.transform = 'translateY(-100%)'
})()

const shift_down = (elem, i) => {
    if (i == 0)
        elem.style.transform = 'translateY(100%)'
    else if (i > 1)
        elem.style.transform = `translateY(${-(i - 1) * 100}%)`
    else
        elem.style.transform = 'translateY(0)'

}