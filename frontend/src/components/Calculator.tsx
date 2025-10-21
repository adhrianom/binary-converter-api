import React, { useEffect, useState } from 'react';
import './Calculator.css';
import { convertToIEEE754, type ConverterResponse } from '../api';

function Calculator() {
  const [ieee, setIeee] = useState<ConverterResponse | null>(null);
  const [input, setInput] = useState('');
  const [animate, setAnimate] = useState(false);
  const [lastOperation, setLastOperation] = useState('');
  const [isResult, setIsResult] = useState(false);

  useEffect(() => {
    setAnimate(true);
    const timer = setTimeout(() => setAnimate(false), 400);
    return () => clearTimeout(timer);
  }, [input]);

  function inputNum(e: React.MouseEvent<HTMLButtonElement>) {
    const value = e.currentTarget.value;
    if (isResult && !isNaN(Number(value))) {
      setInput(value);
      setIsResult(false);
      setShowOperation(false);
      setLastOperation('');
    } else {
      setInput((prev) => prev + value);
      setIsResult(false);
      setShowOperation(false);
      setLastOperation('');
    }
  }

  function clear() {
    setInput('');
    setShowOperation(false);
    setIeee(null);
    setLastOperation('');
  }

  function deleteNum() {
    setInput((prev) => prev.slice(0, -1));
  }

  function calculate() {
    try {
      setLastOperation(input);
      let sanitized = input.replace(/\b0+(\d)/g, '$1');
      sanitized = sanitized.replace(/[\+\-\*\/]+$/, '');
      setLastOperation(sanitized);
      const result = eval(sanitized);
      setInput(result.toString());
      setShowOperation(true);
      setIsResult(true);
    } catch {
      setInput('Error');
      setIsResult(true);
    }
  }

  const [showOperation, setShowOperation] = useState(false);

  const convert = async () => {
    const value = Number(input);
    if (isNaN(value)) return;
    try {
      const data = await convertToIEEE754(value);
      setIeee(data);
    } catch (error) {
      console.error('Error converting to IEEE754:', error);
    }
  };

  return (
    <>
      <div className="background">
        <div className="calculator-shadow"></div>
        <div className="calculator">
          <div className={`operation${animate ? ' operation-animate' : ''}`}>
            {showOperation ? lastOperation : ''}
          </div>
          <h1 className="input" id="result">
            {input || '0'}
          </h1>
          {ieee && (
            <div className="ieee-result">
              <p>
                {ieee.ieee754.signal} {ieee.ieee754.exponent}{' '}
                {ieee.ieee754.mantissa}
              </p>
            </div>
          )}
          <button className="ieee" onClick={convert}>
            IEEE
          </button>
          <div className="buttons-container">
            <button className="button grey" onClick={clear}>
              Ac
            </button>
            <button className="button grey" onClick={deleteNum}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
              >
                <path
                  d="M6.53499 3H21C21.2652 3 21.5196 3.10536 21.7071 3.29289C21.8946 3.48043 22 3.73478 22 4V20C22 20.2652 21.8946 20.5196 21.7071 20.7071C21.5196 20.8946 21.2652 21 21 21H6.53499C6.3704 21 6.20835 20.9594 6.06321 20.8818C5.91807 20.8042 5.79434 20.6919 5.70299 20.555L0.369993 12.555C0.260354 12.3907 0.201843 12.1975 0.201843 12C0.201843 11.8025 0.260354 11.6093 0.369993 11.445L5.70299 3.445C5.79434 3.30808 5.91807 3.19583 6.06321 3.11821C6.20835 3.04058 6.3704 2.99998 6.53499 3ZM7.06999 5L2.40399 12L7.06999 19H20V5H7.06999ZM13 10.586L15.828 7.757L17.243 9.172L14.414 12L17.243 14.828L15.828 16.243L13 13.414L10.172 16.243L8.75699 14.828L11.586 12L8.75699 9.172L10.172 7.757L13 10.586Z"
                  fill="#A5A5A5"
                />
              </svg>
            </button>
            <button
              className="button dark-blue"
              id="divisor"
              onClick={inputNum}
              value="/"
            >
              /
            </button>
            <button
              className="button dark-blue"
              id="multiplicador"
              onClick={inputNum}
              value="*"
            >
              *
            </button>
            <button className="button dark-grey" onClick={inputNum} value="7">
              7
            </button>
            <button className="button dark-grey" onClick={inputNum} value="8">
              8
            </button>
            <button className="button dark-grey" onClick={inputNum} value="9">
              9
            </button>
            <button className="button dark-blue" onClick={inputNum} value="-">
              -
            </button>
            <button className="button dark-grey" onClick={inputNum} value="4">
              4
            </button>
            <button className="button dark-grey" onClick={inputNum} value="5">
              5
            </button>
            <button className="button dark-grey" onClick={inputNum} value="6">
              6
            </button>
            <button
              className="button dark-blue add"
              onClick={inputNum}
              value="+"
            >
              +
            </button>
            <button className="button dark-grey" onClick={inputNum} value="1">
              1
            </button>
            <button className="button dark-grey" onClick={inputNum} value="2">
              2
            </button>
            <button className="button dark-grey" onClick={inputNum} value="3">
              3
            </button>
            <button className="button blue" onClick={calculate}>
              =
            </button>

            <button
              className="button dark-grey zero"
              onClick={inputNum}
              value="0"
              style={{ gridColumn: 'span 2' }}
            >
              0
            </button>
            <button
              className="button dark-grey dot"
              onClick={inputNum}
              value="."
            >
              .
            </button>
          </div>
        </div>
      </div>
    </>
  );
}

export default Calculator;
