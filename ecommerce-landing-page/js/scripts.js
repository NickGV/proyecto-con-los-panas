async function loadComponent(id, file) {
  try {
    const response = await fetch(`components/${file}`);
    const text = await response.text();
    document.getElementById(id).innerHTML = text;
  } catch (error) {
    console.error(`Error al cargar el componente ${file}:`, error);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  loadComponent("navbar", "navbar.html");
  loadComponent("hero", "hero.html");
  loadComponent("products", "products.html");
  loadComponent("subscription", "subscription.html");
  loadComponent("footer", "footer.html");
});
