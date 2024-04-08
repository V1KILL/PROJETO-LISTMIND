
function AddMembro() {
    Swal.fire({
        title: '<p>Novo Cliente</p>',
        html: `
            <input id="nome" class="swal2-input" placeholder="Nome" autocomplete="off">
            <textarea id="descricao" class="swal2-textarea" placeholder="Defeito Relatado"></textarea>
            <div>
                <select id="opcao" class="swal2-select">
                    <option value="0">Serviço</option>
                    <option value="1">Diagnóstico</option>
                    <option value="2">Compra</option>
                </select>
            </div>
            <input class="swal2-input" type="date" id="predicted-date" name="predicted-date"><br><br>
            <input id="predicted-preco" class="swal2-input" placeholder="Valor Previsto" type="number" autocomplete="off" required>
            <input id="preco" class="swal2-input" placeholder="Valor Pago" type="number" autocomplete="off" required>
            <textarea id="servico" class="swal2-textarea" placeholder="Serviço a Ser Executado"></textarea>
            <textarea id="peca" class="swal2-textarea" placeholder="Peças Aplicadas"></textarea>
        `,
        
        confirmButtonText: 'Adicionar Cliente',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#19C37D',
        cancelButtonColor: '#d33',
        
        showLoaderOnConfirm: true,
        showCancelButton: true,
        preConfirm: () => {
            const name = Swal.getPopup().querySelector('#nome').value;
            const preco = Swal.getPopup().querySelector('#preco').value;
            const defeito = Swal.getPopup().querySelector('#descricao').value;
            const opcao = Swal.getPopup().querySelector('#opcao').value;
            const predictedDate = Swal.getPopup().querySelector('#predicted-date').value;
            const predictedPreco = Swal.getPopup().querySelector('#predicted-preco').value;
            const servico = Swal.getPopup().querySelector('#servico').value;
            const peca = Swal.getPopup().querySelector('#peca').value;

            if (!name || !preco || !defeito || !opcao || !predictedDate || !predictedPreco || !servico || !peca) {
                Swal.showValidationMessage('Todos os campos são obrigatórios');
                return false;
            }

            
            window.location.href = `/addclient/${name}/${defeito}/${opcao}/${predictedDate}/${predictedPreco}/${preco}/${servico}/${peca}`;
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

function Document(id){
    window.open(`/document/${id}`, '_blank');
}