import React, {useState, useEffect} from "react";

const Dropdown = ({ options, onSelect }) => {
    const [selectedOption, setSelectedOption] = useState(options[0]);
  
    useEffect(() => {
      onSelect(selectedOption);
    }, [selectedOption, onSelect]);
  
    return (
      <select
        value={selectedOption}
        onChange={(e) => setSelectedOption(e.target.value)}
      >
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    );
};

export default Dropdown;