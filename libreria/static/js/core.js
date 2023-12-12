function deleteBook(button) {
  let urlId = button.getAttribute('data-url');
  Swal.fire({
    title: "¿Estás seguro?",
    text: "¡Esta acción no se puede revertir!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#FF0000",
    cancelButtonColor: "#6C757D",
    confirmButtonText: "Eliminar",
    cancelButtonText: "Salir",
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: "Éxito",
        text: "¡Libro eliminado correctamente!",
        icon: "success",
      });
      setTimeout(() => {
        window.location.href = urlId;
      }, 2000);
    }
  });
}