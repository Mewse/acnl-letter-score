import React from 'react';

const DetailCheckList = (props) => {
    return (
        <div className="table-responsive">
            <table className="table table-hover table-bordered">
                <thead>
                    <tr>
                        <th scope="col" className="w-25">Check</th>
                        <th scope="col">Rule</th>
                        <th scope="col" className="w-25">Points</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Punctuation</td>
                        <td>
                            +10 for every capital letter within 3 characters after punctuation, -10 if not present.
                            +20 for the final character being punctuation ("?", ".", "!")
                        </td>
                        <td className={props.punctuationScore > 0 ? "table-success" : "table-danger" }>{props.punctuationScore}</td>
                    </tr>
                    <tr>
                        <td>Trigrams</td>
                        <td>
                            +1 for every word that starts with a common trigram multiplied by 3
                        </td>
                        <td className={props.trigramScore > 0 ? "table-success" : "table-danger" }>{props.trigramScore}</td>
                    </tr>
                    <tr>
                        <td>Capital</td>
                        <td>
                            +20 If the first non-space character is a capital. Otherwise, -10
                        </td>
                        <td className={props.capitalScore > 0 ? "table-success" : "table-danger" }>{props.capitalScore}</td>
                    </tr>
                    <tr>
                        <td>Repetition</td>
                        <td>
                            -50 if you repeat the same character 3 times in a row anywhere in your message
                        </td>
                        <td className={props.repetitionScore >= 0 ? "table-success" : "table-danger" }>{props.repetitionScore}</td>
                    </tr>
                    <tr>
                        <td>Space-Ratio</td>
                        <td>
                            -20 If the number or spaces divided by the total character count of your message is below 0.2. Otherwise, +20
                        </td>
                        <td className={props.spaceRatioScore > 0 ? "table-success" : "table-danger" }>{props.spaceRatioScore}</td>
                    </tr>
                    <tr>
                        <td>Length</td>
                        <td>
                            -150 if your message is over 75 characters and you have a section of text that goes 75 characters without punctuation.
                        </td>
                        <td className={props.lengthScore >= 0 ? "table-success" : "table-danger" }>{props.lengthScore}</td>
                    </tr>
                    <tr>
                        <td>Spaces</td>
                        <td>
                            +20 for every 32 character block that contains a space. -20 for every block that doesn't.
                        </td>
                        <td className={props.spaceScore > 0 ? "table-success" : "table-danger" }>{props.spaceScore}</td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            Total:
                        </td>
                        <td>{props.total}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
};

export default DetailCheckList;