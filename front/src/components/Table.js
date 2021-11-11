import React from 'react';

function Table({data}) {


    return (
        <div className={'container'}>
            <ul>
                {data.map(item =>
                    <li key={item.id}>
                        {item.name}
                        {item.mark}
                    </li>
                )}
            </ul>
        </div>
    )
}

export default Table;