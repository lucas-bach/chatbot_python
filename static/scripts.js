document.addEventListener('DOMContentLoaded', function() {
    // Adiciona um evento de confirmação para links de exclusão
    const deleteLinks = document.querySelectorAll('a.delete-link');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            const confirmed = confirm('Tem certeza de que deseja excluir esta tarefa?');
            if (!confirmed) {
                event.preventDefault(); // Cancela o clique se o usuário não confirmar
            }
        });
    });

    // Adiciona um evento para marcar tarefas como concluídas
    const completeLinks = document.querySelectorAll('a.complete-link');
    completeLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Impede o redirecionamento padrão
            const url = this.href;
            
            // Atualiza a tarefa como concluída usando fetch
            fetch(url, { method: 'GET' })
                .then(response => {
                    if (response.ok) {
                        // Atualiza a interface do usuário
                        this.textContent = this.textContent === 'Mark as Completed' ? 'Completed' : 'Mark as Completed';
                    } else {
                        console.error('Erro ao atualizar a tarefa.');
                    }
                })
                .catch(error => console.error('Erro:', error));
        });
    });
});
