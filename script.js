document.getElementById('cgpaForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const currentCGPA = parseFloat(document.getElementById('currentCGPA').value);
    const totalCreditsCompleted = parseFloat(document.getElementById('totalCreditsCompleted').value);
    const desiredCGPA = parseFloat(document.getElementById('desiredCGPA').value);
    const futureCredits = parseFloat(document.getElementById('futureCredits').value);

    const totalQualityPoints = currentCGPA * totalCreditsCompleted;
    const requiredQualityPoints = desiredCGPA * (totalCreditsCompleted + futureCredits);
    const futureCGPA = (requiredQualityPoints - totalQualityPoints) / futureCredits;

    const resultDiv = document.getElementById('result');
    if (futureCGPA > 4.0) {
        resultDiv.textContent = 'It is not possible to achieve the desired CGPA with the given future credits.';
    } else {
        resultDiv.textContent = `You need an average CGPA of ${futureCGPA.toFixed(2)} in your future courses to achieve your desired CGPA.`;
    }
});
