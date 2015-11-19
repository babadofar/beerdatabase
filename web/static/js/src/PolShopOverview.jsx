var bd = this.bd || {};
(function (ns) {
    'use strict';


    var columns = ns.getColumnsForTable(['name', 'brewery', 'style', 'rating', 'price']);

    columns.push({
            id: 'stock',
            name: 'Antall',
            formatter: function (beer) {
                return beer.stock;
            },
            sortParams: 'stock',
            isSorted: false,
            sortDirection: 'asc'
    });

    var PolShopOverview = React.createClass({

        render: function () {
            return (
                <div>
                    <h1>{this.props.shop.name}</h1>
                    <div className='row'>
                        <div className='four columns'>
                            <strong>Kategori</strong><br />
                            {this.props.shop.category}
                        </div>
                        <div className='four columns'>
                            <strong>Gateadresse</strong>
                            <address>
                              {this.props.shop.street_address}<br/>
                              {this.props.shop.street_zipcode}{' '}{this.props.shop.street_place}<br />
                            </address>
                        </div>
                        <div className='four columns'>
                            <strong>Postadresse</strong>
                            <address>
                              {this.props.shop.post_address}<br/>
                              {this.props.shop.post_zipcode}{' '}{this.props.shop.post_place}<br />
                            </address>

                        </div>
                    </div>
                    <div className='row'>

                        <div className='twelve columns'>
                            <h3>Tilgjengelige øl ({this.props.beers.length})</h3>
                            <ns.SortableTable items={this.props.beers} columns={columns} />
                        </div>
                    </div>
                </div>
            );
        }

    });

    ns.renderPolShopOverview = function(polShop, beers, component) {
        ReactDOM.render(<PolShopOverview shop={polShop} beers={beers} />, component);
    };

}(bd));