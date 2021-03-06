var bd = this.bd || {};
(function (ns) {
    'use strict';

    var columns = [
        {
            id: 'name',
            name: 'Navn',
            formatter: function (brewery) {
                return (<a href={'/breweries/' + brewery.id}>{brewery.name}</a>);
            },
            sortParams: 'name',
            isSorted: true,
            sortDirection: 'asc'
        },
        {
            id: 'country',
            name: 'Land',
            formatter: function (brewery) {
                return brewery.country.name;
            },
            sortParams: ['country', 'name'],
            isSorted: false,
            filterable: true,
            sortDirection: 'asc'
        },
        {
            id: 'num_beers',
            name: 'Antall øl på polet',
            formatter: function (brewery) {
                return brewery.num_beers_polet;
            },
            sortParams: 'num_beers_polet',
            isSorted: false,
            sortDirection: 'desc'
        }
    ];

    function getColumnsForTable(columnIds) {
        return _.filter(columns, function (column) {
            return (columnIds.indexOf(column.id) > -1);
        });
    }

    ns.renderBreweyTable = function(breweryList, columnIds, component) {
        breweryList = breweryList.sort(ns.Util.getSorter(['name'], false));
        var columnsForTable = getColumnsForTable(columnIds);
        ReactDOM.render(
            <ns.SortableTable
                items={breweryList}
                filterable={true}
                columns={columnsForTable} />,
            component
        );
    };

    ns.renderBreweryListPage = function (breweries, componentId, title) {

        var columns = getColumnsForTable(['name', 'country', 'num_beers']);
        var component = document.getElementById(componentId);
        ReactDOM.render(
            <ns.Container
                component={ns.SortableTable}
                title={title}
                items={breweries}
                filterable={true}
                columns={columns} />,
            component
        );
    };

}(bd));
