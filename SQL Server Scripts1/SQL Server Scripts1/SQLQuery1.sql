USE CustomerFeedbackDB;


SELECT Feedback_Categories.Category_Name, COUNT(*) AS Feedback_Count
FROM Feedback
JOIN Feedback_Categories ON Feedback.CategoryID = Feedback_Categories.Category_ID
GROUP BY Feedback_Categories.Category_Name;

 