from textblob.classifiers import NaiveBayesClassifier

train = [
    # Negotiations
    ('What is the current status of the negotiations?', 'negotiations'),
    ('Have the negotiation terms been finalized?', 'negotiations'),
    ('Are the peace talks progressing well?', 'negotiations'),
    ('When is the next negotiation meeting scheduled?', 'negotiations'),
    ('What are the key points in the negotiation agenda?', 'negotiations'),
    
    # Disagreement
    ('I disagree with the proposed approach.', 'disagreement'),
    ('There is a conflict regarding the contract terms.', 'disagreement'),
    ('We have differing opinions on this matter.', 'disagreement'),
    ('The team is divided over the new policy.', 'disagreement'),
    ('Several members expressed their dissent.', 'disagreement'),
    
    # Attire
    ('What is the dress code for the event?', 'attire'),
    ('Is formal wear required for the gala?', 'attire'),
    ('What should I wear to the conference?', 'attire'),
    ('Are jeans acceptable for the casual day?', 'attire'),
    ('Do we need to wear business casual?', 'attire'),
    
    # Progress
    ('How do you assess the progress of the project?', 'progress'),
    ('Can you update me on the project milestones?', 'progress'),
    ('What progress has been made so far?', 'progress'),
    ('The development phase is nearly complete.', 'progress'),
    ('Are we on track to meet our deadlines?', 'progress'),
    
    # Agreement
    ('We have reached a satisfactory agreement.', 'agreement'),
    ('Both parties have signed the agreement.', 'agreement'),
    ('We concur with the outlined plan.', 'agreement'),
    ('An agreement has been reached by all members.', 'agreement'),
    ('The contract has been mutually agreed upon.', 'agreement')
]

def entrenamiento():
    return NaiveBayesClassifier(train)
