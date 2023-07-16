-- Create stored procedure ComputeAverageScoreForUser
-- Compute the average score for the user
-- Update the user's average_score attribute
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;

    UPDATE users SET average_score = avg_score WHERE id = user_id;
END $$
DELIMITER ;

