document.addEventListener("DOMContentLoaded", () => {
    const exportBtn = document.querySelector(".btn");
    const deleteBtn = document.querySelector(".btn-danger");

    exportBtn.addEventListener("click", () => {
        alert("Fonction d’export des données à implémenter !");
    });

    deleteBtn.addEventListener("click", () => {
        const confirmDelete = confirm("Voulez-vous vraiment supprimer toutes les données ?");
        if (confirmDelete) {
            alert("Données supprimées (simulation).");
        }
    });
});
