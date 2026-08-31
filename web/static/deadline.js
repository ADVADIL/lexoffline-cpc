document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('category-select');
    const ruleSelect = document.getElementById('rule-select');
    const rulesDataElement = document.getElementById('rules-data');
    
    if (!categorySelect || !ruleSelect || !rulesDataElement) return;

    let rulesData = [];
    try {
        rulesData = JSON.parse(rulesDataElement.textContent);
    } catch (e) {
        console.error("Failed to parse rules data:", e);
        return;
    }

    // Store the currently selected rule (from server render)
    const initialSelectedRule = ruleSelect.value;

    function populateRules(selectedCategory) {
        // Clear current options
        ruleSelect.innerHTML = '<option value="">Select a rule...</option>';
        
        // Filter rules
        const filteredRules = selectedCategory 
            ? rulesData.filter(r => r.category === selectedCategory)
            : rulesData;
            
        // Populate options
        filteredRules.forEach(rule => {
            const option = document.createElement('option');
            option.value = rule.key;
            option.textContent = `${rule.label} (${rule.provision})`;
            
            if (rule.key === initialSelectedRule) {
                option.selected = true;
            }
            
            ruleSelect.appendChild(option);
        });
    }

    categorySelect.addEventListener('change', function() {
        populateRules(this.value);
    });

    // Initialize on page load (in case category was pre-selected or to load all)
    // Only repopulate if we didn't just get rendered fully populated by the backend,
    // actually, let's always repopulate to ensure consistency with JS state.
    populateRules(categorySelect.value);
});
