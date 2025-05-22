document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('new-board-btn').addEventListener('click', async function () {
        try {
            const response = await fetch("/new_board");
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const data = await response.json();
            console.log("Received board data:", data);
            updateBoard(data.board);
        } catch (error) {
            console.error('Fetch error:', error);
            alert("Failed to load new board. See console for details.");
        }
    });

    document.getElementById('solve-btn').addEventListener('click', async () => {
        try {
            const board = [];
            for (let row = 0; row < 9; row++) {
                board[row] = [];
                for (let col = 0; col < 9; col++) {
                    const cell = document.getElementById(`cell-${row}-${col}`);
                    board[row][col] = cell.value === '' ? '.' : cell.value;
                }
            }

            console.log("Sending board to solve:", board);

            const response = await fetch("/solve", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ board: board }),
            });

            if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
            const data = await response.json();
            console.log("Solved board received:", data.solved_board);
            updateBoard(data.solved_board);
        } catch (error) {
            console.error("Solve failed:", error);
            alert(`Solve failed: ${error.message}`);
        }
    });

    document.getElementById('check-btn').addEventListener('click', async () => {
        try {
            const board = [];
            for (let row = 0; row < 9; row++) {
                board[row] = [];
                for (let col = 0; col < 9; col++) {
                    const cell = document.getElementById(`cell-${row}-${col}`);
                    board[row][col] = cell.value === '' ? 0 : parseInt(cell.value);
                }
            }

            const response = await fetch("/check", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ board: board }),
            });

            const result = await response.json();

            const message = document.getElementById('message');
            if (result.valid) {
                message.textContent = "✅ Correct! Well done!";
                message.style.color = 'green';
            } else {
                message.textContent = "❌ Incorrect solution. Keep trying!";
                message.style.color = 'red';
            }

        } catch (error) {
            console.error("Check failed:", error);
            alert("Failed to validate board. See console for details.");
        }
    });

    function updateBoard(board) {
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                const cell = document.getElementById(`cell-${row}-${col}`);
                const value = board[row][col];
                cell.value = value === 0 || value === '.' ? '' : value;

                if (value !== 0 && value !== '.') {
                    cell.classList.add('prefilled');
                    cell.readOnly = true;
                } else {
                    cell.classList.remove('prefilled');
                    cell.readOnly = false;
                }
            }
        }
    }
});
