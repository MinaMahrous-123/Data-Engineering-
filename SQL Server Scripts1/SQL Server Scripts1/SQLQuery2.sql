CREATE TABLE Feedback_Fact (
    Feedback_ID INT PRIMARY KEY,
    Customer_ID INT,
    Category_ID INT,
    Feedback_Date DATE,
    Feedback_Text TEXT
);
 
CREATE TABLE Customer_Dimension (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(255),
    Age INT,
    Gender VARCHAR(50)
);

INSERT INTO Feedback_Fact
SELECT FeedbackID, CustomerID, CategoryID, FeedbackDate, FeedbackText
FROM Feedback;

INSERT INTO Customer_Dimension
SELECT CustomerID, Name, Age, Gender
FROM Customers;
