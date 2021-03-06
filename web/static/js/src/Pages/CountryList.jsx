var bd = this.bd || {};
(function (ns) {
    'use strict';

    var columns = [
        {
            id: 'name',
            name: 'Navn',
            formatter: function (country) {
                return (<a href={'/countries/' + country.rb_id}>{country.name}</a>);
            },
            sortParams: 'name',
            isSorted: false,
            sortDirection: 'asc'
        },
        {
            id: 'count_pol',
            name: 'Antall øl på polet',
            formatter: function (country) {
                return country.count;
            },
            sortParams: 'count',
            isSorted: true,
            sortDirection: 'desc'
        }
    ];

    ns.renderCountryList = function (countries, componentId, title) {
        var component = document.getElementById(componentId);
        ReactDOM.render(
            <ns.Container
                component={ns.SortableTable}
                title={title}
                items={countries}
                columns={columns}
                idProperty="rb_id" />,
            component
        );
    };

}(bd));
