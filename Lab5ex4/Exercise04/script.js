const questions = [
  {
    text: "What does HTML stand for?",
    options: ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyperlink Text Management Language"],
    correct: 1
  },
  {
    text: "Which language is used for styling web pages?",
    options: ["HTML", "JQuery", "CSS"],
    correct: 2
  },
  {
    text: "Inside which HTML element do we put JavaScript?",
    options: ["<js>", "<script>", "<javascript>"],
    correct: 1
  }
];

let currentIndex = 0;
let score = 0;

const questionText = document.getElementById("questionText");
const optionsContainer = document.getElementById("optionsContainer");
const resultEl = document.getElementById("result");

function loadQuestion() {
  const current = questions[currentIndex];
  questionText.innerText = current.text;
  optionsContainer.innerHTML = "";

  current.options.forEach((option, idx) => {
    const btn = document.createElement("button");
    btn.className = "option";
    btn.innerText = option;
    btn.onclick = () => selectAnswer(idx);
    optionsContainer.appendChild(btn);
  });
}

function selectAnswer(selected) {
  if (selected === questions[currentIndex].correct) {
    score++;
  }
  nextQuestion();
}

function nextQuestion() {
  currentIndex++;
  if (currentIndex < questions.length) {
    loadQuestion();
  } else {
    showResult();
  }
}

function showResult() {
  document.getElementById("quizBox").style.display = "none";
  resultEl.innerText = `Your score: ${score} / ${questions.length}`;
}

// Start
loadQuestion();
