const parallaxMenu = document.getElementById("parallax-menu");

Array.from(document.getElementsByClassName("parallax-menu-item"))
  .forEach((item, index) => {
    item.onmouseover = () => {
        parallaxMenu.dataset.activeIndex = index;
    }
  });