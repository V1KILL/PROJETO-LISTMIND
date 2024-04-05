
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



function Mudar(id, status, name, description) {
    let checkbox;
    let isChecked = 'False';
    if (status == 'True') {
        isChecked = 'checked';
    }
    Swal.fire({
        title: `${name}`,
        html:
           `<input id="nome" class="swal2-input" placeholder="Nome" autocomplete="off" value=${name}>
            <textarea id="descricao" class="swal2-textarea" placeholder="Descrição" >${description}</textarea>
                
            <div class="checkbox-container">
                <input id="feito" type="checkbox" class="swal2-checkbox" ${isChecked}>
                <label for="feito" class="swal2-checkbox-label">Feito</label>
                <div>
                    <a href="/clientdelete/${id}" id="excluir" class="swal2-a">Excluir Cliente</a>
                </div>
            </div>`,

        confirmButtonText: 'Editar',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#19C37D',
        cancelButtonColor: '#d33',
        showCancelButton: true,
       

        preConfirm: () => {
            const nome = document.getElementById('nome').value;
            const descricao = document.getElementById('descricao').value;
            const checkbox = document.getElementById('feito').checked;

            // Validação do input
            
            if (!nome.trim() || !descricao.trim()) {
                Swal.showValidationMessage('O Título e a Descrição Não Podem Ser Vazios');
                return false;
              }

            return { nome: nome, descricao: descricao, checkbox: checkbox };
        },
        
    }).then(result => {
        if (result.isConfirmed) {
            const { nome, descricao, checkbox } = result.value;
            window.location.href = `/serviceedit/${checkbox}/${id}/${nome}/${descricao}`;
        }
    });

}