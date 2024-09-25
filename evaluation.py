def evaluate_omr(extracted_answers, answer_key):
    score = 0
    total_questions = len(answer_key)
    result = []
    
    for question_num, selected_answer in extracted_answers.items():
        correct_answer = answer_key[question_num]
        if selected_answer == correct_answer:
            result.append(f"Question {question_num}: {selected_answer} (Correct)")
            score += 1
        else:
            result.append(f"Question {question_num}: {selected_answer} (Wrong), Correct: {correct_answer}")
    result.append(f"Total Score: {score}/{total_questions}")
    return result
extracted_answers = {1: 'A', 2: 'B', 3: 'C'} 
answer_key = {1: 'A', 2: 'C', 3: 'C'} 
evaluation_result = evaluate_omr(extracted_answers, answer_key)
for line in evaluation_result:
    print(line)
