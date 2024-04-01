
function AddMembro() {
    Swal.fire({
        title: '<p>Novo Cliente</p>',
        html: `
            <input id="nome" class="swal2-input" placeholder="Nome" autocomplete="off">
            <input id="telefone" class="swal2-input" placeholder="Telefone" type="tel" autocomplete="off">
            <input id="preco" class="swal2-input" placeholder="Preço" type="number" autocomplete="off" required>
            <textarea id="descricao" class="swal2-textarea" placeholder="Descrição"></textarea>
        `,
        
        confirmButtonText: 'Adicionar Cliente',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#19C37D',
        cancelButtonColor: '#d33',
        showLoaderOnConfirm: true,
        showCancelButton: true,
        preConfirm: () => {
            const name = Swal.getPopup().querySelector('#nome').value;
            const price = Swal.getPopup().querySelector('#preco').value;
            const phonenumber = Swal.getPopup().querySelector('#telefone').value;
            const description = Swal.getPopup().querySelector('#descricao').value;

            if (!name.trim() || !price.trim() || !phonenumber.trim() || !description.trim()) {
                Swal.showValidationMessage('Todos os campos são obrigatórios');
                return false;
            }
            window.location.href = `/addclient/${name}/${phonenumber}/${price}/${description}`;
        },
        allowOutsideClick: () => !Swal.isLoading(),
    });
}



function Mudar(id, status) {
    let checkbox;
    let isChecked = 'False';
    if (status == 'True') {
        isChecked = 'checked';
    }
    Swal.fire({
        title: "Editar Serviço",
        html:
           // `<input id="nome" class="swal2-input" placeholder="Nome" autocomplete="off">
            //<textarea id="descricao" class="swal2-textarea" placeholder="Descrição"></textarea>
                
            `<div class="checkbox-container">
                <input id="feito" type="checkbox" class="swal2-checkbox" ${isChecked}>
                <label for="feito" class="swal2-checkbox-label">Feito</label>
            </div>`,

        showCancelButton: true,
        confirmButtonText: "Salvar",
        cancelButtonText: "Cancelar",
        allowOutsideClick: false,
        preConfirm: () => {
            
            const checkbox = document.getElementById('feito').checked;
            return checkbox.checked

           
        },
        
    }).then(result => {
        const checkbox = document.getElementById('feito');
        const isChecked = checkbox.checked; 
        if (result.isConfirmed) {
            window.location.href = `/serviceedit/${isChecked}/${id}`;
        }
    });
}